# Bacon #

Bacon is a utility for building other utilities. It helps generate a template for creating quick utilities run in bash (using alias commands) and written in Python.  In short, Bacon makes everything better!

## Setup ##

First, create a directory called "bash-tools".  Typically, this lives inside your "Documents" folder, but you can create it wherever you like.  Next, `cd` into the `bash-tools` directory. So, for example:

```
cd ~/Documents && mkdir bash-tools
cd bash-tools
```

Now, clone the bacon utility inside your `bash-tools` directory.

```
git clone git@github.com:jaderigby/bacon.git
```

Then, create a `.bashrc` file and add the following:

```
alias bacon="python ~/Documents/bash-tools/bacon/baconActions.py"
```

__Note:__ If you created your `bash-tools` file anywhere else, other than the `Documents` folder, you will need to modify the path above to point to wherever you installed bacon.

Once your .bashrc file is setup, add the following to your `.bash_profile` file.  If you do not have a `.bash_profile` file, you can add it by going to your user's root directory and creating a file called `.bash_profile`:

```
source ~/Documents/bash-tools/.bashrc
```

__You are set!__

If you are using the default setup, ie inside the `Documents` folder, you can run the following commands for your setup:

```
cd ~/Documents && mkdir bash-tools
cd bash-tools
git clone git@github.com:jaderigby/bacon.git
cd ~/Documents/bash-tools/bacon && touch .bashrc
echo "alias bacon=\"python ~/Documents/bash-tools/bacon/baconActions.py\"" >> .bashrc
echo "source ~/Documents/bash-tools/.bashrc" >> .bash_profile
```

## Usage ##

Type `bacon` in order to see the options.

When creating a new utility, do:

```
bacon new
```

This will walk you through creating a new utility.

When adding an action to an existing utility, do:

```
bacon add
```

This will scan the `bash-tools` directory and list all folders, ie all utilities, for selection.  Select the utility which you would like to add an action to.

Utilities observe the following behavior:

- Typing the name of the utility - or rather - its alias, shows the list of possible commands/attributes.

- When invoking a utility, each utility follows the pattern: `<utility-name> <action>`

- Utilities come with a handful of `helpers` when writing your utility, that make writing utilities easier.  These are common `helper` functions covering common actions that a typical utility might use.

## Terminology ##

__Utility:__ A Python script, or collection of scripts, accompanied by a bash alias for invoking said script.

__Attribute:__ A command added to a utility, such as `bacon add` where `add` is the action.

__Bacon:__ A simple utility that makes everything better!

## Structure ##

- __actions.py__ = where the action invocations are defined.
- __messages.py__ = where all messages are to be contained.  This keeps things clean and defined.
- __helpers.py__ = where all common functions should live.  A typical utility will contain any functions not defining specific business logic inside the helpers.py file.
- __settings.py__ = where the settings definitions live.  This file typically does not need to be modified.
- __profiles__ = the profiles folder is where locally-specific settings live.  Any definition specific to a particular developers setup can be defined here.  This is also where any settings or task-specific data/definitions should live.  You can have multiple profile files inside the `profiles` folder.  Change which profile file your utility points to by changing the reference in the utility's `settings.py` file.
- __profile.py__ = an example profile file.
- __status.py__ = the status file is simply for running the `status` attribute in order to verify setup in the beginning. This can be modified and used however you like or you may remove this file and its accompanying reference in the `actions.py` file.
- __action-list.json__ = this is where the actions are described.  When you do `myUtility status`, this file is read, and the names and descriptions are listed. You can use this file to add descriptions for each of your utility's actions.
- __action.py__ = an example of a typical action file.  This can also be removed, along with its reference inside the `actions.py` file.
