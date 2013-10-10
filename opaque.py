from xml.dom.minidom import parse
from os.path import basename, splitext

def set_opaque(filename):
    dom = parse(filename)
    svg = dom.getElementsByTagName('svg')[0]
    for node in svg.childNodes:
        traverse(node)
    newFilename = '_opaque'.join(splitext(basename(filename)))
    print newFilename
    f = open(newFilename, 'w')
    f.write(dom.toxml())
    f.close()
        
def traverse(node):
    if node.hasChildNodes():
        for n in node.childNodes:
            traverse(n)
    attr = node.attributes
    if attr is not None:
        for i in range(attr.length):
            item = attr.item(i)
            if item.name == 'style':
                newStyle = []
                for style in item.value.split(';'):
                    if style.find('opacity') != -1:
                        key, value = style.split(':')
                        newStyle.append(key + ':1')
                    else: 
                        newStyle.append(style)
                node.setAttribute('style', ';'.join(newStyle))
            elif item.name.find('opacity') != -1:
                item.value = '1'
            
    