import pygal


# Create a World Map instance
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

# Add countries for North, Central, and South America
wm.add('North America', ['ca', 'mx', 'us'])  # Canada, Mexico, United States
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])  # Belize, Costa Rica, Guatemala, Honduras, Nicaragua, Panama, El Salvador
wm.add('South America', [
    'ar', 'bo', 'br', 'cl', 'co', 'ec', 'gy', 'py', 'pe', 'sr', 'uy', 've'
])  # Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela

# Render the map to an SVG file
wm.render_to_file('americas.svg')
