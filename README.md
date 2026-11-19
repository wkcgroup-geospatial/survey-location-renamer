What the Script Does

The script automatically generates standardized survey station IDs based on the survey type stored in the DataType field.

Instead of modifying existing site names or labels, the script creates a new field called Labels and stores the generated IDs there. This ensures that original naming conventions and survey records remain unchanged.

Example output:

DataType	Labels
Sherman Trap	ST01
Sherman Trap	ST02
Sherman Trap	ST03
Camera Trap	CT01
Camera Trap	CT02
Vantage Point	VP01
Quadrat	QD01
Expected Data Structure

The input layer should contain a field called:

Field Name	Description
DataType	Survey method or equipment type (e.g., Sherman Trap, Camera Trap, Vantage Point, Quadrat, Transect)

The script will automatically create:

Field Name	Description
Labels	Standardized survey station ID generated from the DataType value

Example input:

DataType
Sherman Trap
Sherman Trap
Camera Trap
Quadrat

Example output:

DataType	Labels
Sherman Trap	ST01
Sherman Trap	ST02
Camera Trap	CT01
Quadrat	QD01
Supported Survey Types

Survey types are mapped to prefixes using a configurable dictionary:

Python
prefix_map = {
"Sherman Trap": "ST",
"Camera Trap": "CT",
"Vantage Point": "VP",
"Quadrat": "QD",
"Transect": "TR",
"Mist Net": "MN",
"Bat Net": "BN",
"Anabat": "AB"
}

Additional survey methods can be added by updating this dictionary.

How to Use
Open QGIS and load the survey location layer.
Ensure that the layer contains a DataType field.
Open the Python Console using Ctrl + Alt + P.
Open the script file (survey_location_renamer.py).
Copy and paste the script into the Python Console.
Review and modify the survey type dictionary if required.
Run the script.
A new field named Labels will be created automatically.
Standardized survey station IDs will be generated and stored in the Labels field.
Notes
Original survey names and existing attributes are preserved.
The script creates a separate Labels field rather than overwriting existing naming conventions.
Numbering is maintained independently for each survey type.
Values are padded with leading zeros (e.g., ST01, ST02, ST03).
Additional survey types can be configured through the prefix dictionary.
Ideal for biodiversity assessments, ecological surveys, environmental impact assessments (EIA), baseline studies, and wildlife monitoring projects.
Example Output
Plain Text
Sherman Trap → ST01
Sherman Trap → ST02
Sherman Trap → ST03
 
Camera Trap → CT01
Camera Trap → CT02
 
Vantage Point → VP01
Vantage Point → VP02
 
Quadrat → QD01
Quadrat → QD02
 
Transect → TR01
Transect → TR02