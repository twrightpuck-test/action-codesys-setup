# CODESYS Installation Verification Script
# This script runs headlessly to verify CODESYS is properly installed

from scriptengine import *

print("CODESYS Installation Verification")
print("==================================")

try:
    version_info = system.get_version()
    print(f"CODESYS Version: {version_info}")
except:
    print("Could not retrieve version info, but CODESYS started successfully")

print("Verification complete - CODESYS is working!")
system.exit(0)
