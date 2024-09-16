from .resource.sheet import Sheet
from .cabinet_type import CabinetType

class Drawer:
    def __init__(self, quantity, height):
        self.quantity = quantity  # Number of drawers
        self.height = height      # Height of each drawer in meters

    def __repr__(self):
        return f"Drawer(quantity={self.quantity}, height={self.height}m)"

class Cabinet:
    def __init__(
        self,
        cabinet_type,
        name,
        length,
        height,
        depth,
        material_interiors,
        back_panel=False,
        material_back_panel=None,
        fronts=False,
        material_fronts=None,
        top=False,
        material_top=None,
        drawers=None,  # Optional Drawer object or list of drawers
        shelf_spacing=None  # Optional shelf spacing in meters
    ):
        self.cabinet_type = cabinet_type  # Instance of CabinetType enum
        self.name = name                  # String
        self.length = length              # Length in meters
        self.height = height              # Height in meters
        self.depth = depth                # Depth in meters
        self.material_interiors = material_interiors  # Sheet, required
        self.back_panel = back_panel      # Boolean, default True
        self.material_back_panel = material_back_panel  # Sheet, optional
        self.fronts = fronts              # Boolean, default False
        self.material_fronts = material_fronts        # Sheet, optional
        self.top = top                    # Boolean, default False
        self.material_top = material_top  # Sheet, optional
        self.drawers = drawers            # Optional Drawer object or list of drawers
        self.shelf_spacing = shelf_spacing  # Optional shelf spacing in meters

        # Validate that materials are provided when required
        if self.back_panel and not self.material_back_panel:
            raise ValueError("Material for back panel must be provided if back panel is included.")
        if self.fronts and not self.material_fronts:
            raise ValueError("Material for fronts must be provided if fronts are included.")
        if self.top and not self.material_top:
            raise ValueError("Material for top must be provided if top is included.")

    def calculate_drawer_space(self):
        """Calculate the total height used by the drawers."""
        if self.drawers:
            return self.drawers.quantity * self.drawers.height
        return 0

    def __repr__(self):
        return (f"Cabinet(name='{self.name}', type={self.cabinet_type}, "
                f"dimensions=({self.length}m x {self.height}m x {self.depth}m), "
                f"back_panel={self.back_panel}, fronts={self.fronts}, top={self.top}, "
                f"drawers={self.drawers}, shelf_spacing={self.shelf_spacing})")
