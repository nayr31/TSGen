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
long_desc = input("Please input a long description of your mod (this will be displayed on the main page):\n")
print("\nPlease list your dependencies by a single number.\nIf a dependency relies on something (otherloader relies on deli), you don't need to put both.")
print("1 - BepInEx")
print("2 - Deli")
print("3 - OtherLoader")
print("4 - Sodalite")
print("5 - Sideloader")
print("6 - [Stop listing dependencies]")
dependency_list = []
while True:
    dep_input = input("\nInput number: ")
    if dep_input == "1":
        print("Adding BepInEx Dependency")
        dependency_list.append("BepInEx-BepInExPack_H3VR-5.4.1101")
    elif dep_input == "2":
        print("Adding Deli Dependency")
        dependency_list.append("DeliCollective-Deli-0.4.1")
    elif dep_input == "3":
        print("Adding OtherLoader Dependency")
        dependency_list.append("devyndamonster-OtherLoader-0.3.0")
    elif dep_input == "4":
        print("Adding Sodalite Dependency")
        dependency_list.append("nrgill28-Sodalite-1.0.0")
    elif dep_input == "5":
        print("Adding Sideloader Dependency")
        dependency_list.append("denikson-H3VR_Sideloader-0.3.6")
    elif dep_input == "6":
        print("Stopping dependency list...")
        break
json_data["dependencies"] = dependency_list

print("Making folder...")
path = os.path.join(home_dir, json_data["name"])
os.mkdir(path)
os.chdir(path)

print("Attempting to write...")
with open("manifest.json", "w+") as f:
    json.dump(json_data, f)
with open("README.md", "w+") as outfile:
    outfile.write("# " + json_data["name"] + "\n\n")
    outfile.write(long_desc)
src = os.path.join(home_dir, "icon_template.png")
dst = os.path.join(path, "icon.png")
shutil.copyfile(src, dst)