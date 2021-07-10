import os, json, shutil

home_dir = os.getcwd()

print("Working in " + home_dir)

#print("Loading manifest template...")
with open("manifest_template.json", "r+") as f:
    json_data = json.load(f)

json_data["name"] = input("Please input your mod name: ").replace(" ", "_")
json_data["version_number"] = input("Please input your version number (x.x.x): ")
json_data["website_url"] = input("Website url? You can leave this blank: ")
json_data["description"] = input("Write a short description of your mod: ")
long_desc = input("Input a long description of your mod (this will be displayed on the main page):\n")

print("\nLoading Dependency list...")

with open("Dependencies.json", "r+") as f:
    json_dependencies = json.load(f)

print("Please list your dependencies by a single number.\nIf a dependency relies on something (otherloader relies on deli), you don't need to put both.")

dep_pos = 0

for dep_pos in range(0, len(json_dependencies["dependency-name"])):
    print(str(dep_pos) + " - " + json_dependencies["dependency-name"][dep_pos])

print(str(dep_pos + 1) + " - [Stop listing dependencies]")

dependency_list = []
while True:
    dep_input = input("\nInput number: ")

    if dep_input < len(json_dependencies["dependency-name"]):
        print("Adding " + json_dependencies["dependency-name"][dep_input] + "(" + json_dependencies["dependency-tag"] + ")")
        dependency_list.append(json_dependencies["dependency-tag"][dep_input])
    elif dep_input == len(json_dependencies["dependency-name"]):
        print("Stopping dependency list...")
        break
json_data["dependencies"] = dependency_list

print("Making folder...")
path = os.path.join(home_dir, json_data["name"])
os.mkdir(path)
os.chdir(path)

print("Attempting to write...")
with open("manifest.json", "w+") as f:
    json.dump(json_data, f, indent=2)
with open("README.md", "w+") as outfile:
    outfile.write("# " + json_data["name"] + "\n\n")
    outfile.write(long_desc)
src = os.path.join(home_dir, "icon_template.png")
dst = os.path.join(path, "icon.png")
shutil.copyfile(src, dst)