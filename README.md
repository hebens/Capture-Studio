
This program is in early development, and will provide when finalized:

  * A graphical user interface with separate frames for input, buttons, and clipboard entry list.
  * Ability to add new clipboard entries by pasting from system clipboard.
  * Display of stored clipboard entries in a scrollable listbox.
  * Selection of an entry to insert back into the main input field.
  * Clear All button to remove all saved entries.
  * Persistent storage using shelve module so that entries are preserved between program restarts.

Key features:
  * The program uses Tkinter for creating GUI components.
  * Entries are stored in a dictionary with unique keys and displayed as key-value pairs in the listbox.
  * pyperclip is used to interact with system clipboard.
  * Shelve module provides persistent storage of clipboard contents across sessions.
  * Listbox allows easy navigation through saved entries.

To use this program:
  * Copy text you want to save using standard copy command (Ctrl+C).
  * Click "Add" button - the content will be stored in the listbox.
  * Select an entry from the listbox and click "Insert" or double-click on it to insert back into the input field.
  * Use "Clear All" to remove all saved entries.

The program saves clipboard contents periodically, so you won't lose your data when closing the application.
