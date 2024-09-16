import csv

def export_pieces_to_csv(pieces, filepath):
    """Exports a list of pieces to a CSV file with the given filepath."""
    
    # Define the CSV header
    header = ['cant', 'base', 'height', 'details', 'rotates', 'edgeBand_upp', 'edgeBand_low', 'edgeBand_lef', 'edgeBand_rig']

    # Open the file for writing
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header to the CSV file
        writer.writerow(header)

        # Write each piece's data using __repr__
        for piece in pieces:
            writer.writerow(piece.__repr__().split(','))
