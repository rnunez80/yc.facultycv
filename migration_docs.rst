========
Migrating CV's in yc.facultycv
========

Note: This documentation contains important information regarding migrating content from an existing site with the Products.FacultyCV currently running over to a new Plone 6 site running yc.facultycv.

Requirements Prior to Migration:
--------------------------------

- You must be logged into the CMS as an admin user.
- Both sites must have collective.exportimport installed as the python scripts use dependencies from it.
- On your "old" site, download the yc.facultycv Plone add-on from the develop branch since it contains the "voltomigration" python script.
- On your "new" site, download the yc.facultycv Plone add-on from the main branch since it contains the "voltoimport" python script used to import the CV's.
- Notice: If you cannot switch over to the "develop" branch in the old site for any reason, upload the "voltomigration.pt" AND the "voltomigration.py" into the site root of the CMS (not the root-root)!
- You will need to run buildout or mxdev to update the dependencies if not done so already.
- On the old site you will need: plone.app.dexterity == 2.4.7, plone.restapi == 7.8.1, plone.dexterity == 2.5.0, plone.supermodel == 1.5.0, plone.rest == 2.0.0, plone.schema == 1.2.1, and PyJWT == 1.7.1.

Instructions for Migration:
___________________________

- Point the web browser to "/@@cvmigration" to begin the in-place migration process on the old site.
- Point the web browser to "directory/{cv shortname or item id goes here}/@@voltomigration" for the old site.
- Check the "select all/none" box as well as the "include revisions" box in the menu.
- Click Export to export the data to the local machine or the server (if selected as so).
- Assuming, on the new site, that yc.facultycv is installed successfully, add a new "directory" type at the root of the Plone site.
- Point the web browser to the new location of the faculty cv in the Plone Classic site since the exportimport does not have a Volto interface as of now.
- Go to "/@@voltoimport" in the web browser at the new site.
- Upload the downloaded JSON file by clicking browse.
- Check the desired options.
- Click import.
- Check what got imported. If all goes well, there should be a populated directory folder in the new site.
