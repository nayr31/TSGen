import os, json, shutil, requests

home_dir = os.getcwd()

print("Working in " + home_dir)

print("Loading manifest template...\n")
with open("manifest_template.json", "r+") as f:
    json_data = json.load(f)

## Get general information from user
json_data["name"] = input("Please input your mod name: ").replace(" ", "_")
json_data["version_number"] = input("Please input your version number (x.x.x): ")
json_data["website_url"] = input("Website url? You can leave this blank: ")
json_data["description"] = input("Write a short description of your mod: ")
long_desc = input("Input a long description of your mod (this will be displayed on the main page):\n")

print("\nLoading Dependency list...")
## Check to see if dependency list is out of date
try:
    dep_url = "https://raw.githubusercontent.com/nayr31/TSGen/main/Dependencies.json"
    dep_file = requests.get(dep_url, stream=True)
    with open("Dependencies_temp.json", "wb") as f:
        f.write(dep_file.content)
except:
    print("There was an error downloading/writing the Dependency file.\nPlease run TSGen as admin or download the file manually from the github page.")
    input()
    exit

with open("Dependencies.json", "r+") as f:
    json_dependencies = json.load(f)
with open("Dependencies_temp.json", "r+") as f:
    json_check = json.load(f)

# If its out of date, write the new file
if(json_dependencies["version"] < json_check["version"]):
    print("Dependeny list is out of date, updating...")
    json_dependencies["version"] = json_check["version"]
    json_dependencies["dependency-name"] = json_check["dependency-name"]
    json_dependencies["dependency-tag"] = json_check["dependency-tag"]
    with open("Dependencies.json", "w+") as f:
        json.dump(json_dependencies, f, indent=2)
# Always remove old checking file
os.remove("Dependencies_temp.json")

## Get a list of dependencies from the user
print("Please list your dependencies by a single number.\nIf a dependency relies on something (otherloader relies on deli), you don't need to put both.")

# Set up dependency array from read file
dep_pos = 0
for dep_pos in range(0, len(json_dependencies["dependency-name"])):
    print(str(dep_pos) + " - " + json_dependencies["dependency-name"][dep_pos])
print(str(dep_pos + 1) + " - [Stop listing dependencies]")

# Create an empty list and parse the data from the user
dependency_list = []
while True:
    dep_input = int(input("\nInput number: "))
    
    if dep_input < len(json_dependencies["dependency-name"]):
        print("Adding " + json_dependencies["dependency-name"][dep_input] + " (" + json_dependencies["dependency-tag"][dep_input] + ")")
        dependency_list.append(json_dependencies["dependency-tag"][dep_input])
    elif dep_input == len(json_dependencies["dependency-name"]):
        print("Stopping dependency list...")
        break
    else:
        print("That wasn't a valid number from the list, only type the number.")
# Save that list to the data set
json_data["dependencies"] = dependency_list

## Create the folder for the files to rest into
print("Making folder...")
path = os.path.join(home_dir, json_data["name"])
os.mkdir(path)
os.chdir(path)

## Write the data collected into a json, and copy the image file
print("Attempting to write...")
with open("manifest.json", "w+") as f:
    json.dump(json_data, f, indent=2)
with open("README.md", "w+") as outfile:
    outfile.write("# " + json_data["name"] + "\n\n")
    outfile.write(long_desc)
src = os.path.join(home_dir, "icon_template.png")
dst = os.path.join(path, "icon.png")
shutil.copyfile(src, dst)

print("\nYour mod files have been copied to " + os.getcwd() + ".")
print("Please change the icon to something custom, modify the README file to add pictures or formatting.")

print("\nINSTALLATION:")
print("Add the generated files to a zip file, along with your mod files.")
print("Anything that goes into the BepInEx/plugins folder (.deli, .dll) can be directly added to the zip file.")
print("Sideloader mods need to be placed into the Sideloader folder inside of your zip \"MyMod.zip/Sideloader\"")
print("Legacy assetbundle support is purely manual, and should not be uploaded to Thunderstore.")
input()