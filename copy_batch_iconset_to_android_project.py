#!/usr/bin/python
# Copyright (C) 2013 Herbert Straub herbert@linuhacker.at
# License: GNU / GPL

import os, shutil, sys
  
class IconCopy:
  def __init__( self, iconName, projectPath ):
    self.sizes = {
      "drawable-mdpi" : "32x32",
      "drawable-hdpi" : "48x48",
      "drawable-xhdpi" : "64x64",
    }
    self.pngPrefix = "MENU-PNG"
    self.iconName = iconName
    self.projectPath = projectPath

  def checkIcons( self ):
    success = True
  
    for size in self.sizes:
      if not os.path.exists( "%s/%s/%s" % ( self.pngPrefix, self.sizes[size], self.iconName ) ):
	print "%s for size %s not exists" % ( self.iconName, size )
	success = False
  
    return success
  
  def checkProjectPath( self ):
    if not os.path.exists( self.projectPath ):
      print "%s not exists"
      return False
    if not os.path.exists( "%s/res" % self.projectPath ):
      print "%s/res not exists"
      return False
    return True
  
  def copyIcon( self ):
    print "Copy Icon %s to %s" % ( self.iconName, self.projectPath )
    for size in self.sizes:
	outputPath = "%s/res/%s" % ( self.projectPath, size )
	iconFile = "%s/%s/%s" % ( self.pngPrefix, self.sizes[size], self.iconName )
	if os.path.exists( outputPath ):
	  shutil.copy( iconFile, outputPath)
	  print "  copied to %s" % size
	else:
	  print "  %s not exists" % size 
  
  
if __name__ == "__main__":
  


  if len( sys.argv ) != 3:
    print "%s icon_filename android_project_path" % sys.argv[0]
    sys.exit( 1 )
  
  iconCopy = IconCopy( sys.argv[1], sys.argv[2] )  

  if not iconCopy.checkIcons( ):
    sys.exit( 1 )
    
  if not iconCopy.checkProjectPath( ):
    sys.exit( 1 )
    
  iconCopy.copyIcon( )