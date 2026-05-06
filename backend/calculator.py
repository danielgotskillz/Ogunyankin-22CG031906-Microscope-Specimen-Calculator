MICROSCOPE_FACTORS = {
    "Light Microscope (40x)": 40,
    "Light Microscope (100x)": 100,
    "Electron Microscope (1000x)": 1000,
    "Electron Microscope (5000x)": 5000,
}

UNIT_CONVERSION = {
    "nm": 1e9,
    "µm": 1e6,
    "mm": 1e3,
    "cm": 1e2,
    "m": 1,
}

def calculate_real_size(image_size, microscope_type, unit):
    magnification = MICROSCOPE_FACTORS[microscope_type]
    
    real_size_meters = image_size / magnification
    converted_size = real_size_meters * UNIT_CONVERSION[unit]

    breakdown = f"""
    Step 1: Measured size = {image_size}
    Step 2: Magnification = {magnification}x
    Step 3: Real size (meters) = {image_size} / {magnification} = {real_size_meters}
    Step 4: Converted to {unit} = {converted_size}
    """

    return converted_size, breakdown