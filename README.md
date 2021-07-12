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

## FAQ/Problems

**Q.** Why do I need this?

**A.** You don't, especially since you are changing most of the files afterwards (or at least its recommended to). All thats required from Thunderstore are specific files that most users would have trouble with diagnosing. This program aims to free the user from that hassle so you can simply open it, write your information easily, then upload in as little time as possible. [Here](https://user-images.githubusercontent.com/69859977/125286887-48690980-e2ea-11eb-951d-112717259444.png) is an image of the contents needed for upload. Thunderstore will block any upload that does not follow this guideline.


**Q.** [Insert anti-virus software here] said that `TSGen.exe` was a virus!

**A.** Because of the nature of how the file was downloaded and how its packaged, most anti-virus softwares will be hesitant to use it. You have every right to avoid using this software. At the time of this being written, there are 2 alternitives in delevelopement.

**Q.** No folder or files are being made after I finish typing in my information!

**A.** There are a few things that might have happened:
- You didn't stop listing dependency strings
  - As it prompts you to input a number for each dependency, there will be one option that says `X - [Stop listing dependencies]`, where X is a number. Input that number.
- The program is unable to write to the directory you extracted it to
  - There are some cases where you can add files to a folder, but you can't change/edit them. This is a permissions problem, and running it as admin will fix it.

If you have any other problems/questions, message the creator @gamernayr#8165 on discord.
