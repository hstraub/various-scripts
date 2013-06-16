#!/usr/bin/python
# Copyright (C) 2013 Herbert Straub herbert@linuhacker.at
# License: GNU / GPL

# Instructions:
# 1. Download the Batch iconset from http://adamwhitcroft.com/batch/
# 2. cd Downloads
# 3. unzip Batch-master.zip
# 4. create a working directory: mkdir ~/icons
# 5. cd ~/icons
# 6. mkdir SVG-ORIGINAL
# 7. cp ~/Downloads/Batch-master/SVG/* SVG-ORIGINAL/
# 8. mkdir SVG-HOLO-LIGHT
# 9. convert python batch_iconset_convert.py
#
# You can find the converted icons in the Subdirectory MENU_PNG
#
# See: http://developer.android.com/guide/practices/ui_guidelines/icon_design.html

import lxml, lxml.etree, os, subprocess


def convertOneSVGFile( inputFile, outputFile ):
  parser = lxml.etree.XMLParser( )
  doc = lxml.etree.parse( inputFile, parser )
  
  nsmap = { 'svg' : 'http://www.w3.org/2000/svg' }
  
  svgElement = doc.xpath( "/svg:svg", namespaces=nsmap )[0]
  svgAttributes = svgElement.attrib
  color = svgElement.get( "fill" )
  svgElement.set( "fill", "#333333" )
  svgElement.set( "fill-opacity", "0.6" )
  svgElement.set( "transform", "scale(0.75) translate(7,7)" )

  fh = open( outputFile, "w" ) 
  fh.write( lxml.etree.tostring( doc, pretty_print=True ) )
  fh.close( )
  

if __name__ == "__main__":
  svgInputDir = "SVG-ORIGINAL"
  svgOutputDir = "SVG-HOLO-LIGHT"
  pngSizes = [ "32x32", "48x48", "64x64" ]

  for pngSize in pngSizes:
    try:
      os.makedirs( "MENU-PNG/%s" % pngSize )
    except:
      pass
  
  for filename in os.listdir( svgInputDir ):
    imageMagickInputFile = "%s/%s" % ( svgOutputDir, filename )
    outputFilename = "ic_menu_%s" % filename.replace( ".svg", ".png" ).replace( "-", "_" )
    try:
      convertOneSVGFile( "%s/%s" % ( svgInputDir, filename ) , "%s/%s" % ( svgOutputDir, filename ) )
    except Exception as e:
      print "Error modifying %s/%s: %s" % ( svgInputDir, filename, e )
      continue
    
    for pngSize in pngSizes:
      outputFile = "MENU-PNG/%s/%s" % ( pngSize, outputFilename )
      subprocess.call( "convert -background none -resize %s %s %s" % (
	pngSize, imageMagickInputFile, outputFile ), shell=True )
