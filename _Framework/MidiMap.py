#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/_Framework/MidiMap.py
from __future__ import absolute_import
import Live
from .ButtonMatrixElement import ButtonMatrixElement
from .ButtonElement import ButtonElement
from .EncoderElement import EncoderElement
from .SliderElement import SliderElement

def make_button(name, channel, number, midi_message_type):
    is_momentary = True
    return ButtonElement(not is_momentary, midi_message_type, channel, number, name=name)


def make_slider(name, channel, number, midi_message_type):
    return SliderElement(midi_message_type, channel, number, name=name)


def make_encoder(name, channel, number, midi_message_type):
    return EncoderElement(midi_message_type, channel, number, Live.MidiMap.MapMode.absolute, name=name)


class MidiMap(dict):

    def add_button(self, name, channel, number, midi_message_type):
        raise name not in self.keys() or AssertionError
        self[name] = make_button(name, channel, number, midi_message_type)

    def add_matrix(self, name, element_factory, channel, numbers, midi_message_type):
        raise name not in self.keys() or AssertionError

        def one_dimensional_name(base_name, x, _y):
            return '%s[%d]' % (base_name, x)

        def two_dimensional_name(base_name, x, y):
            return '%s[%d,%d]' % (base_name, x, y)

        name_factory = two_dimensional_name if len(numbers) > 1 else one_dimensional_name
        elements = [ [ element_factory(name_factory(name, column, row), channel, identifier, midi_message_type) for column, identifier in enumerate(identifiers) ] for row, identifiers in enumerate(numbers) ]
        self[name] = ButtonMatrixElement(rows=elements)