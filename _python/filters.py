def dateformat(value, format="%d-%b-%Y"):
    return value.strftime(format)

filters = {}
filters['dateformat'] = dateformat

def filtercontent(sections,url="/tech/"):
    for section in sections:
        if section['url'] == url:
            return section['content']
    return []

filters['filtercontent'] = filtercontent
