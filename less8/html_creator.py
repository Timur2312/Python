from user_interface import temperature_viwe
from user_interface import wind_speed_viwe
from user_interface import pressure_viwe

def create(device = 1):
    style = 'style="font-size:22px"'
    html = '<html>\ <head></head>\n <body>\n'
    html += '      <p {}> Temperature: {} c</p>\n'\
                .format(style,temperature_viwe(device))
    html += '      <p {}>Wind_speed: {} m/s</p>\n'\
                .format(style,wind_speed_viwe(device))
    html += '     <p {}>Pressure: {} mmHg</p>\n'\
                .format(style,pressure_viwe(device))
    html += '   </body>\n</html>'

    with open('index.html','w') as page:
        page.write(html)
    
    return html

def new_create(data,device = 1):
    t, p, w = data
    style = 'style="font-size:22px"'
    html = '<html>\ <head></head>\n <body>\n'
    html += '      <p {}> Temperature: {} c</p>\n'\
                .format(style,t)
    html += '      <p {}>Wind_speed: {} m/s</p>\n'\
                .format(style,w)
    html += '     <p {}>Pressure: {} mmHg</p>\n'\
                .format(style,p)
    html += '   </body>\n</html>'

    with open('new_index.html','w') as page:
        page.write(html)
    
    return data