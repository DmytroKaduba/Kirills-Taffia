from classes import Room

#Create the room (map_uni)
none = Room('', '', '', '')
room_hall = Room('Hall', 'You enter a long hall with various portraits on the walls.', {'north' : 'Reception'}, ['notebook'] )
room_reception = Room('Reception', 'You enter the main reception of the building. The room is empty.', {'south': 'Hall', 'west':'Cafe', 'north': 'Class', 'east':'Office'},[])
room_office = Room('Office', 'You step into a well iluminated office with a paintig of a snowy landscape on the wall.',{'west' : 'Reception'}, ['notebook'] )
room_cafe = Room('Cafe', 'Before you is a busy cafe. The barista is strugling to keep up with the work load and looks at you desperately as you walk in.', {'east' : 'Reception'}, ['notebook'] )
room_class = Room('Class', 'You enter an empty class room. On the black board you notice a complicated equation.', {'south' : 'Reception'}, ['notebook'] )

#room dictionary for navigation
map_uni = {
    'Reception' : room_reception,
    'Hall' : room_hall,
    'Office': room_office,
    'Cafe': room_cafe,
    'Class': room_class
}
