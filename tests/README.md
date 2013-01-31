To run the tests, you'll need to have installed Python's `nose`
package. Then execute this command in the top-level project directory
(or this directory):

    $ nosetests --nologcapture

The `--nologcapture` flag is necessary because `nose` will interfere
with `salt-cloud`'s log capturing otherwise.
