For my personal website, I have been building upon several different functions I want to run on there.
This includes a blog feature that I can update wherever and whenever I want as long as the server is active.

This project involves running a Flask web server and is coded in mostly python.

For the purpose of this blog function, you will need to have two different command prompt or terminal windows for the blog to function.

You will need the latest version of python installed.
Check to see if you have this installed by using

python --version

On Linux, the package for python installation is 'python3', and the command will depend on your distribution.

On Windows, the installer is available in their Downloads section on https://www.python.org/.

After cloning the library, you may need to also install flask. Navigate to the 'blogassignment' directory and install flask by using pip

pip install flask

Again, you will need two different terminal windows for this function. In the first window, activate the server by using

python web.py

The default location for the website is "localhost:5000." Go to this location in your web browser to view the site.

All other buttons are placeholders. Click on the 'Blog' button to view the blog. You should see a placeholder post.

In a second terminal window, launch newpost.py to create a new post. It will prompt you to first add a title, and then another prompt for the text content. After completion, you should either see a success or failure message for the blog post.

If successful, refresh the blog page to view your new post. This can be done multiple times.

The posts are stored in postlist.json. Because the flask server does not refresh the list when clearing it, if you plan on clearing the blog for testing, you can make a backup copy of postlist.json after running web.py after the first time.