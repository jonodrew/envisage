""" A group in a tool bar or menu. """


# Enthought library imports.
from enthought.traits.api import Any, Bool, HasTraits, Instance, Str

# Local imports.
from location import Location


class Group(HasTraits):
    """ A group in a tool bar or menu. """

    # The group's unique identifier (unique within the tool bar, menu bar or
    # menu that the group is to be added to).
    id = Str

    # Does this group require a separator?
    separator = Bool(True)

    # The location of the group.
    location = Any#Instance(Location)

    # The optional name of a class that implements the group. The class must
    # support the **enthought.pyface.action.Group** interface.
    class_name = Str

    def __str__(self):
        return 'Group(%s)' % self.id

    __repr__ = __str__
    
#### EOF ######################################################################
