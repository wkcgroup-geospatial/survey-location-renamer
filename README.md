**What the Script Does**

The script automatically generates standardized survey station IDs based on the survey type stored in the DataType field.

Instead of modifying existing site names or labels, the script creates a new field called Labels and stores the generated IDs there. This ensures that original naming conventions and survey records remain unchanged.


The input layer should contain a field called:


**Data_Type**	- Survey method or equipment type (e.g., Sherman Trap, Camera Trap, Vantage Point, Quadrat, Transect)

The script will automatically create:

**Labels** -	Standardized survey station ID generated from the DataType value


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

**How to Use**
1. Open QGIS and load the survey location layer.
2. Ensure that the layer contains a Data_Type field.
3. Open the Python Console using Ctrl + Alt + P.
4. Open the script file (survey_location_renamer.py).
5. Copy and paste the script into the Python Console.
6. Review and modify the survey type dictionary if required.
7. Run the script.
8. A new field named Labels will be created automatically.

Standardized survey station IDs will be generated and stored in the Labels field.

**Notes**

Original survey names and existing attributes are preserved.
The script creates a separate Labels field rather than overwriting existing naming conventions.
Numbering is maintained independently for each survey type.
Values are padded with leading zeros (e.g., ST01, ST02, ST03).
Additional survey types can be configured through the prefix dictionary.
Ideal for biodiversity assessments, ecological surveys, environmental impact assessments (EIA), baseline studies, and wildlife monitoring projects.

**Example Output**

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
