from lxml import etree

xmlFile = open('config.xml', "r")
xmlstring = xmlFile.read()
xmlFile.close()
xmlroot = etree.fromstring(xmlstring)

panel_descriptions = xmlroot.find("PanelDescriptions")

if panel_descriptions is not None:
    for child in panel_descriptions:
        if child.tag == "PanelDescription":
            child_str = etree.tostring(child, encoding="unicode")
            print(child_str)
