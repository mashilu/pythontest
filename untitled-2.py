from xml.dom import minidom

xmldoc = minidom.parse("E:\\2_CODE\\0_github\\python\\diveintopython\\xml\\kant.xml")
#print xmldoc.toxml()

#print xmldoc.childNodes

#for node in xmldoc.childNodes:
 #   print node

print xmldoc.lastChild.childNodes