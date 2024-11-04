# Character Creation Manager

Character Manager is a Django-based web application meant to provide a quick reference for users, i.e. regular players and GMs, to be used in TTRPGs. Character Manager is based on the system DND uses but can be adapted. The idea behind this is to be able to quickly review vital character stats like health or status effects, especially when starting a new session.
This app gives users full CRUD functionality for their own characters - they are also able to view other players' characters.
GMs have access to full CRUD functionality to all characters, i.e. their own and other players' characters.
MOSCOW methodology was used to create and priortise user stories as well as update expectations and intended use cases during development.

## Live app
The live app, hosted on heroku, can be found [https://fullstack-character-manager-2b32ce1f5d35.herokuapp.com/] (here).

## Project Features

- **User Authentication and Profiles**: Users can register, log in, and manage their profiles.
- **Character CRUD Functionality**:
  - **Create**: Logged-in users can create characters, setting attributes like name, HP, class, race, and various status effects.
  - **Read**: Users can view character details, including profile images, status effects, and exhaustion levels.
  - **Update**: Character owners, GMs, and admins can edit character details, including uploading or removing profile images.
  - **Delete**: Character owners and GMs can delete characters.
- **Status Effects**: Characters can have a range of status effects (e.g., blinded, stunned, charmed), shown as toggles in the interface.
- **Exhaustion Levels**: Dropdown to set the character's exhaustion level.
- **Profile Image Handling**: Users can upload custom profile images for characters or revert to a default placeholder.

## Project Features not implemented yet
- **Several campaigns**: Possibility to sort and filter characters by different campaigns
- **Dark mode**
- **Switching user roles** Ability to add or delete user roles for existing users without need of use for admin panel

## Testing

## Manual testing ##
1. **User Authentication**: Registration, login, and profile access functionalities were verified.
2. **Character CRUD Operations**:
   - **Creation**: Confirmed that characters are created with unique slugs and owner permissions.
   - **Viewing**: Verified that all character details are displayed as intended.
   - **Editing**: Tested that owners, GMs, and admins can edit characters, including updating and deleting images.
   - **Deletion**: Ensured that only authorized users can delete characters, with appropriate permission handling.
3. **Profile Picture Handling**: Tested the upload functionality and the delete image button, which resets to a default image.
4. **Status Effects and Exhaustion Levels**: Checked that toggles and dropdowns display and save correctly in character profiles.

## Verification
- [https://validator.w3.org](HTML verification)
- [https://jigsaw.w3.org/css-validator](CSS validation)
- Performance testing: Google Lighthouse plugin
- Accessibility testing: Google Silktide plugin

## Python tests
- Basic tests were written to mimic manual testing.

## Figma Design

A wireframe was mocked up using figma. The design was kept very simple and straight forward on purpose to avoid distractions and clutter once multiple characters have been added. The design can be found [https://www.figma.com/design/Q1shSoiRoOmRqhheTyMfZc/Untitled?node-id=0-1&node-type=canvas&t=nuzAnNe7hgC0wUeu-0](here).


## Credits + external tools used

- **Pillow (Django)**: A Django libary found [https://pypi.org/project/pillow/] (here) to simplify profile picture management
- **Contrast checker**: https://webaim.org/resources/contrastchecker/
- **Placeholder SVG**: https://www.svgrepo.com/svg/295402/user-profile
- **Bootstrap documentation**: https://getbootstrap.com/docs/5.0/getting-started/introduction/
- Stackoverflow and general google searches for error codes
- **Status effect list**: https://roll20.net/compendium/dnd5e/Conditions#content


