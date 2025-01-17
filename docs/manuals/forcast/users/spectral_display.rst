Extracted spectra are displayed in an interactive plot window, for
data analysis and visualization (see |ref_spectral|).

The spectral display tool has a number of useful features and controls.
See |ref_eye_controls| and the table below for a quick summary.


.. table:: Spectral Viewer controls
   :class: longtable
   :widths: 30 30 40

   +-----------------------------------+---------------------------+------------------------+
   | **Feature**                       | **Control**               | **Keyboard shortcut**  |
   +===================================+===========================+========================+
   | Load new FITS file                | *File Choice -> Add File* |  --                    |
   +-----------------------------------+---------------------------+------------------------+
   | Remove loaded FITS file           | *File Choice ->*          |  Press *delete* in the |
   |                                   | *Remove File*             |  *File Choice* panel   |
   +-----------------------------------+---------------------------+------------------------+
   | Plot selected file                | *File Choice ->*          |  --                    |
   |                                   | *(double-click)*          |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Add a new plot window (pane)      | *Panes ->*                |  --                    |
   |                                   | *Add Pane*                |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Remove a pane                     | *Panes ->*                |  Press *delete* in the |
   |                                   | *Remove Pane*             |  *Panes* panel, or in  |
   |                                   |                           |  the plot window       |
   +-----------------------------------+---------------------------+------------------------+
   | Show or hide a plot               | *Panes -> Pane # ->*      |  --                    |
   |                                   | *File name -> Enabled*,   |                        |
   |                                   | or click the *Hide all*/  |                        |
   |                                   | *Show all* button         |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Display a different X or Y        | *Axis ->*                 |  --                    |
   | field (e.g. spectral error,       | *X Property* or           |                        |
   | transmission, or response)        | *Y Property*              |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Overplot a different Y axis       | *Axis ->*                 |  --                    |
   | field (e.g. spectral error,       | *Overplot -> Enabled*     |                        |
   | transmission, or response)        |                           |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Change X or Y units               | *Axis ->*                 |  --                    |
   |                                   | *X Unit* or               |                        |
   |                                   | *Y Unit*                  |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Change X or Y scale               | *Axis ->*                 |  --                    |
   |                                   | *X Scale* or *Y Scale*    |                        |
   |                                   | *-> Linear* or *Log*      |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Interactive zoom                  | *Axis -> Zoom*:           |  In the plot window,   |
   |                                   | *X*, *Y*, *Box*,          |  press *x*, *y*, or    |
   |                                   | then click in the plot    |  *z* to start zoom mode|
   |                                   | to set the limits; or     |  in x-direction,       |
   |                                   | *Reset* to reset the      |  y-direction, or box   |
   |                                   | limits to default.        |  mode, respectively.   |
   |                                   |                           |  Click twice on the    |
   |                                   |                           |  plot to set the new   |
   |                                   |                           |  limits.  Press *w*    |
   |                                   |                           |  to reset the plot     |
   |                                   |                           |  limits to defaults.   |
   +-----------------------------------+---------------------------+------------------------+
   | Fit a spectral feature            | --                        |  In the plot window,   |
   |                                   |                           |  press *f* to start    |
   |                                   |                           |  the fitting mode.     |
   |                                   |                           |  Click twice on the    |
   |                                   |                           |  plot to set the data  |
   |                                   |                           |  limits to fit.        |
   +-----------------------------------+---------------------------+------------------------+
   | Change the feature or baseline    | *Analysis -> Feature,*    |  --                    |
   | fit model                         | *Background*              |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Load a spectral line list for     | *Analysis -> Reference*   |  --                    |
   | overplot display                  | *Data: Open, Load List*   |                        |
   |                                   |                           |                        |
   |                                   | Select a one- or two-     |                        |
   |                                   | column text file          |                        |
   |                                   | containing wavelengths in |                        |
   |                                   | microns and (optionally)  |                        |
   |                                   | labels for the values.    |                        |
   |                                   | Columns may be comma,     |                        |
   |                                   | space, or '\|' separated. |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Clear zoom or fit mode            | --                        |  In the plot window,   |
   |                                   |                           |  press *c* to clear    |
   |                                   |                           |  guides and return to  |
   |                                   |                           |  default display mode. |
   +-----------------------------------+---------------------------+------------------------+
   | Change the plot color cycle       | *Plot ->                  |  --                    |
   |                                   | Color cycle ->            |                        |
   |                                   | Accessible*, *Spectral*   |                        |
   |                                   | or *Tableau*              |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Change the plot type              | *Plot -> Plot type ->     |  --                    |
   |                                   | Step*, *Line*, or         |                        |
   |                                   | *Scatter*                 |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Change the plot display options   | *Plot ->                  |  --                    |
   |                                   | Show markers*,            |                        |
   |                                   | *Show errors*,            |                        |
   |                                   | *Show grid*, or           |                        |
   |                                   | *Dark mode*               |                        |
   +-----------------------------------+---------------------------+------------------------+
   | Display the cursor position       | *Cursor panel* ->         |  --                    |
   |                                   | Check *Cursor Location*   |                        |
   |                                   | for a quick display or    |                        |
   |                                   | press *Popout* for full   |                        |
   |                                   | information               |                        |
   +-----------------------------------+---------------------------+------------------------+
