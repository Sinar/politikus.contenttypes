# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s politikus.contenttypes -t test_issue_source.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src politikus.contenttypes.testing.POLITIKUS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/politikus/contenttypes/tests/robot/test_issue_source.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Issue Source
  Given a logged-in site administrator
    and an add Issue form
   When I type 'My Issue Source' into the title field
    and I submit the form
   Then a Issue Source with the title 'My Issue Source' has been created

Scenario: As a site administrator I can view a Issue Source
  Given a logged-in site administrator
    and a Issue Source 'My Issue Source'
   When I go to the Issue Source view
   Then I can see the Issue Source title 'My Issue Source'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Issue form
  Go To  ${PLONE_URL}/++add++Issue

a Issue Source 'My Issue Source'
  Create content  type=Issue  id=my-issue_source  title=My Issue Source

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Issue Source view
  Go To  ${PLONE_URL}/my-issue_source
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Issue Source with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Issue Source title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
