class RemoteControl:

    def __init__(self, tv, room) -> None:
        self.tv = tv
        self.room = room

    def advance_channel(self):
        print('Advance Channel')

    def back_channel(self):
        print('Back Channel')

    def choose_channel(self, channel):
        print('Changed to channel: {}'.format(channel))


control_room = RemoteControl('samsung', 'living room')

print(control_room.room)
print(control_room.tv)

control_room.advance_channel()
control_room.choose_channel(12)


control_bedroom = RemoteControl('LG', 'bed room')
print(control_bedroom.room)
print(control_bedroom.tv)

control_bedroom.advance_channel()
control_bedroom.choose_channel(32)
