# SimToggle

from os import path
from subprocess import call, check_output
import sys

def most_recent_app_bundle():
    '''Find most recently deployed app bundle'''
    iPhone_simulator_dir = "~/Library/Application\\ Support/iPhone\\ Simulator"
    all_apps = check_output("mdfind -onlyin " + iPhone_simulator_dir + " kMDItemContentType = 'com.apple.application-bundle'", shell=True).splitlines()
    return path.dirname(all_apps[0])

def setting_plist_in_app_bundle(bundle):
    '''Locate the preferences plist'''
    pref_dir = bundle + "/Library/Preferences"
    plists = check_output("mdfind -onlyin \"" + pref_dir + "\" kMDItemContentType = 'com.apple.property-list'", shell=True).splitlines()
    return plists[0]

def toggle_setting(pref_setting):
    '''Toggle a preference setting'''
    plist_file = setting_plist_in_app_bundle(most_recent_app_bundle())

    current_value = check_output(["defaults", "read", plist_file, pref_setting]).splitlines()[0]
    toggled_value = "NO" if (current_value == "1") else "YES";
    call(["defaults", "write", plist_file, pref_setting, "-bool", toggled_value])

if __name__ == "__main__":
    toggle_setting(sys.argv[1])
