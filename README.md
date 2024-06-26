# Bacon #

__Note:__ These instructions target mac and unix setups, atm.

Bacon is a utility for building other utilities. It helps generate a template for creating quick utilities run in bash (using alias commands) and written in Python.  In short, Bacon makes everything better!

## Setup ##

First, make sure that you have [git](https://git-scm.com/downloads) installed.

Then, run the following command:

```
cd ~/Documents && mkdir bacon-bits && cd bacon-bits && git clone https://github.com/jaderigby/bacon.git && scp bacon/.baconrc .baconrc && echo '\nsource ~/Documents/bacon-bits/.baconrc' >> ~/.zshrc && source ~/.zshrc
```

What it does:

- Goes to your `Documents` folder and creates a new folder called `bacon-bits`
- Clones the `bacon` repo to the `bacon-bits` folder
- copies the `.baconrc` file from `bacon` to the `bacon-bits` folder
- adds `source ~/Documents/bacon-bits/.baconrc` to your `.zshrc` file
- __Note:__ the last line of the above command runs `source ~/.zshrc`

To verify that the install was successful, run `bacon`. You should see the commands available for bacon.

__You are all set!__

## Made With Bacon! ##

If a utility says "≈≈≈ Made With Bacon!", it belongs in the bacon-bits folder (see Setup instructions above).  To activate, run `bacon alias` and then `bacon set`, and you're all set!

## Yay, Bacon! Now what? ##

Create a new utility, by running:

```
bacon new
```

Follow the instructions in the terminal to finish creating your utility. 

The `name` is the name that will be used for the utility's folder. The alias is the string you will use to trigger your utility. Example: `bacon`.

### Terminology ###

__Utility:__ A Python script, or collection of scripts, accompanied by a bash alias for invoking those scripts.

__Trigger Word:__ A reference to the alias that triggers your utility

__Action:__ A command added to a utility, such as `bacon new` where `new` is the action.

__Bacon:__ A simple utility that makes everything better!

### Adding An Action ###

To add an action to your utility, do:

```
triggerWord -action
```

`bacon new` is an example of an action, where `new` is the action.

You can also add an action that supports parameters, by doing:

```
triggerWord -action args:true
```

This will create a new action which can receive additional parameters as key/value pairs, seperated by a colon, such as:

```
triggerWord create name:test
```

The above command will result in the following object being assigned to your utility's action "argDict" variable:

```
{"name" : "test"}
```

This can be consumed as `argDict['name']` resulting in the value `test`. For example, you could use it to create a new file called "test.txt", like so:

```
helpers.write_file(argDict['name'] + '.txt', contents)
```

### Profiling ###

If you want to create a profile file for your utility, do:

```
triggerWord -profile
```

Profile files are used to set or override your utility's settings file.

### Use The Source! ###

Each time you create a new utility (which adds a new alias to your `bacon-bits/.baconrc` file, you will want to run `bacon set`.  This will source the `.baconrc` file.

### Utilities Observe The Following Behavior: ###

- Typing the trigger word - the alias - shows the list of possible commands/actions.

- When invoking a utility, each utility follows the pattern: `<trigger-word> <action>`

- Utilities come with a handful of `helpers` when writing your utility, that make writing utilities faster and easier.  These are common `helper` functions covering common actions that a typical utility might use.

## Structure ##

- __actions.py__ = where the action invocations are defined.
- __messages.py__ = where all messages are to be contained.  This keeps things clean and neat.
- __helpers.py__ = where all common functions should live.  A typical helpers file will contain any functions not defining specific business logic.
- __settings.py__ = where the settings definitions live.  This file typically does not need to be modified. Exceptions include things such as when you need to switch between multiple profile files, etc.
- __profiles folder__ = the profiles folder is where locally-specific settings live.  Any definition specific to a particular developers setup can be defined here, within a `profile.py` file.  This is also where any settings or task-specific data/definitions should live.  You can have multiple profile files inside the `profiles` folder.  Change which profile file your utility points to by changing the reference in the utility's `settings.py` file.
- __sizzle.py__ = this runs when using the `-action`, `-profile`, or similar commands. Essentially `sizzle.py` contains those features tied to the initial configuration of a utility.
- __profiles/profile.py__ = this is where locally-specific info can be stored/configured. For example, if two developers are using a utility, but have different configurations for that utility, the `profile.py` file is where these unique parts would live.
- __action-list.json__ = this is where the actions are described.  When you do your utility alias with no accompanying action command, this file is read, and the names and descriptions are listed. You can use this file to add descriptions for each of your utility's actions.

## Helpers ##

The helpers file is where you can include the functions that your utility uses.  This file is intended to include any non-business logic.  Bacon utilities come pre-configured with a handful of useful helper functions already.  These are listed below:

- __path('user')__ = returns the user's root directory path, such as doing `cd ~/`
- __path('util')__ = returns the directory path for the utility.
- __load_profile()__ & __get_settings()__ = these two functions are set up specifically for calling the settings.  If you want to use the settings in an action file, uncomment the commented settings line at the top of the file.
- __read_file()__ = opens a specified file.
- __write_file()__ = writes to a specified file with the data being passed in as the second parameter.
- __run_command()__ = runs a specified bash command. Also, it has an optional secondary parameter which accepts a boolean, to supress the output message. Example: `run_command('pwd', False)`. __Note:__ This can be a string or a list of single commands (each command to be chained together as a seperate item within the list, such as ['git', 'push']).
- __run_command_output()__ = runs a specified command and then returns the output.  Also, it has an optional secondary parameter which accepts a boolean, to supress the output message. Example: `run_command_output('pwd', False)`
- __user_input()__ = used to capture user inputs.
- __user_selection()__ = converts a specified list to an interactive selection, where each list item is numbered.  The first argument determins the string given as the input prompt.  If "x" is selected, or enter is pressed before a selection is made, then the function returns the string "exit".  Any other selection that is not a number, returns the error "Please select a valid entry" and allows the user to try again.
- __arguments()__ = use this to create a dictionary object for multiple command-line arguments.

## The Bacon Profile File ##

In addition to your utility having profiles, bacon has support for its own `profile.py` file, as well.  In fact, if you are installing bacon anywhere else other than `Documents`, you can use the profile.py file to make it work.  Observe the following:

- __homeDir__ = to change the location to anything other than `Documents`, such as `"homeDir" : "Development"`. This would reference the `Development` directory, rather than the default `Documents` directory.
- __utilitiesPrimeDirectory__ = to change the bacon home folder to anything other than `bacon-bits`.

To use these, do:

```
bacon -profile
```

This will create the `profiles` directory, and a file called `profile.py`.  Add the following to this file:

```
{
    "settings" : {

    }
}
```

Then, if you want to use one of the options above, such as `homeDir`, you would add it like so:

```
{
    "settings" : {
        "homeDir" : "Development"
    }
}
```