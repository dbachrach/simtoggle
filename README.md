# SimToggle

Control your iOS app settings through the command line instead of changing settings via the Settings app in the simulator. SimToggle supports any boolean flag in your NSUserDefaults.

## See it in action

First, clone SimToggle to your machine:

```zsh
git clone git@github.com:dbachrach/simtoggle.git
```

`simtoggle.py` is a simple python script which takes one arg, the the NSUserDefaults key to toggle.

```zsh
% python simtoggle.py <setting>
```

For example, if the key you were interested in toggling was `production_mode`, then you would invoke:

```zsh
% python path/to/simtoggle.py production_mode
```

If you're using ZSH, add a function to your `.zshrc` file to keep it short and sweet.

```zsh
function tog-prod() {
    python path/to/simtoggle.py "production_mode"
}
```

Then toggle your app settings with just:

```zsh
% tog-prod
```

Bash users can create an alias in your `.bashrc` file for the same simplicity:

```bash
alias tog-prod="python path/to/simtoggle.py 'production_mode'"
```

## How it works

SimToggle searches for the most recently deployed iOS app to any of your simulators. It then searches for that app's preferences plist. Once found, it can toggle the appropriate setting using the `defaults` command. 

Because SimToggle searches for the most recently deployed app, make sure you have just run your app from XCode before using SimToggle.

## Thanks

Special thanks to [this post](http://www.politepix.com/2011/05/13/open-the-simulator-sandbox-folder-of-the-app-you-just-built-and-ran/) for inspiration.

## Contact

Feel free to [get in touch](mailto:ahdustin@gmail.com) with any questions or suggestions.
