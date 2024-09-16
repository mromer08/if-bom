from .piece_type import PieceType
from .resource.sheet import Sheet

class Piece:
    def __init__(
        self,
        piece_type,
        material,
        quantity,
        width,
        length,
        can_rotate,
        edge_banding_top = False,
        edge_banding_bottom = False,
        edge_banding_left = False,
        edge_banding_right = False
    ):
        self.piece_type = piece_type               # Type of the piece (from PieceType enum)
        self.quantity = quantity                   # Quantity of pieces
        self.width = width                         # Width in meters
        self.length = length                       # Length in meters
        self.can_rotate = can_rotate               # Boolean indicating if the piece can be rotated
        self.edge_banding_top = edge_banding_top           # Boolean, default False
        self.edge_banding_bottom = edge_banding_bottom     # Boolean, default False
        self.edge_banding_left = edge_banding_left         # Boolean, default False
        self.edge_banding_right = edge_banding_right       # Boolean, default False
        self.material = material                   # Sheet material (instance of Sheet)

    def __repr__(self):
        return (f"{self.quantity},{self.width},{self.length},{self.piece_type.value},"
                f"{int(self.can_rotate)},{int(self.edge_banding_top)},{int(self.edge_banding_bottom)},"
                f"{int(self.edge_banding_left)},{int(self.edge_banding_right)}")

