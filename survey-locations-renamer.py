layer = iface.activeLayer()

# Create Label field if it doesn't exist
if 'Label' not in [f.name() for f in layer.fields()]:
    from qgis.PyQt.QtCore import QVariant
    layer.dataProvider().addAttributes([QgsField('Label', QVariant.String)])
    layer.updateFields()

label_idx = layer.fields().indexOf('Label')

# Prefix mapping
prefixes = {
    'Anabat': 'AB',
    'Camera Trap': 'CT',
    'Sherman Trap': 'ST',
    'VP': 'VP','Quadrat': 'QD',
}

# Counters for each subtype
counters = {key: 1 for key in prefixes}

layer.startEditing()

# Sort features by ID for consistent numbering
features = sorted(layer.getFeatures(), key=lambda f: f.id())

for feat in features:
    subtype = feat['Sub_Type']

    if subtype in prefixes:
        prefix = prefixes[subtype]
        label = f"{prefix}{counters[subtype]:02d}"

        layer.changeAttributeValue(
            feat.id(),
            label_idx,
            label
        )

        counters[subtype] += 1

layer.commitChanges()

print("Labels updated successfully.")