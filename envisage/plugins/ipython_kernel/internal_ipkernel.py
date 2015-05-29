""" This code has been inspired from the IPython repository

https://github.com/ipython/ipython/blob/2.x/examples/Embedding/internal_ipkernel.py

"""

from IPython.lib.kernel import connect_qtconsole
from IPython.kernel.zmq.kernelapp import IPKernelApp


def mpl_kernel(gui_backend):
    """ Launch and return an IPython kernel with matplotlib support.

    Parameters
    ----------
    gui_backend -- string
      The GUI mode used to initialize the matplotlib mode. For options, see
      the `ipython --matplotlib` help pages.
    """

    kernel = IPKernelApp.instance()
    kernel.initialize(['python', '--pylab=%s' % gui_backend])
    return kernel


class InternalIPKernel(object):
    """ Represents an IPython kernel and the consoles attached to it.
    """

    def init_ipkernel(self, gui_backend):
        """ Initialize the IPython kernel.

        Parameters
        ----------
        gui_backend -- string
          The GUI mode used to initialize the matplotlib mode. For options, see
          the `ipython --matplotlib` help pages.
        """
        # Start IPython kernel with GUI event loop and mpl support
        self.ipkernel = mpl_kernel(gui_backend)
        # To create and track active qt consoles
        self.consoles = []

        # This application will also act on the shell user namespace
        self.namespace = self.ipkernel.shell.user_ns

    def new_qt_console(self, evt=None):
        """ Start a new qtconsole connected to our kernel. """
        return connect_qtconsole(
            self.ipkernel.connection_file, profile=self.ipkernel.profile
        )

    def cleanup_consoles(self, evt=None):
        """ Kill all existing consoles. """
        for c in self.consoles:
            c.kill()

    def shutdown(self):
        """ Shutdown the kernel.

        Existing IPyhton consoles are killed first.
        """
        self.cleanup_consoles()
        self.ipkernel.shell.exit_now = True
