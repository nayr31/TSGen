# TSGen

This program aims to deal with the biggest problem in Thunderstore migration: creating correct compatible files for uploading. The main problems are incorrect manifests, icon sizes, and not having a readme file.

This project was made possible by [`auto-py-to-exe`](https://pypi.org/project/auto-py-to-exe/).

## Installation:
Extract the `.zip` release file into a folder somewhere on your computer so that the `TSGen.exe` file is outside of a `.zip`.
```
C:/
    Users/
        Me/
            Documents/
                TSGen/
                    TSGen.exe
```

Windows Defender is known to yell at this program. You can check through the ***only*** code in the project [`TSGen.py`](https://github.com/nayr31/TSGen/blob/main/TSGen.py) to verify that the code only creates a folder and some files, taking user information.

## Usage
After installation, run the `TSGen.exe` file. A command window should appear:
![image](https://user-images.githubusercontent.com/69859977/124760418-ba161180-defe-11eb-9cb8-0b514259e235.png)

Simply fill out what it requires and it will create a folder inside of wherever you extracted `TSGen.exe` to named after your mod with the manifest, icon, and readme file containing the bare minimum to upload to Thunderstore. 

**Note:** When uploading to Thunderstore, its good practice to name your `.zip` upload `[authorname]-[modname].zip`. Here is an example: `nayr31-NToolbox.zip`. 

It is **highly** recommended to change the `icon.png` and to add pictures to your `README.md` file. You can find out how to add pictures to markdown [here](https://guides.github.com/features/mastering-markdown/).

## Demonstration:
https://user-images.githubusercontent.com/69859977/124760702-006b7080-deff-11eb-96e0-88541cc98c96.mp4

