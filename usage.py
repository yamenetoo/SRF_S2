
# Example usage


excel_file = 'COPE-GSEG-EOPG-TN-15-0007 - Sentinel-2 Spectral Response Functions 2024 - 4.0.xlsx'

# Get spectral response function for S2A Band 4 (Red)
srf_b4 = get_spectral_response_function(excel_file, 'S2A', 'B04')

# Query at specific wavelengths
print(f"S2A B04 at 665 nm: {srf_b4(665.0):.8f}")
print(f"S2A B04 at 664 nm: {srf_b4(664.0):.8f}")
print(f"S2A B04 at 670 nm: {srf_b4(670.0):.8f}")
print(f"S2A B04 at 500 nm (outside): {srf_b4(500.0):.8f}")

# Get function for multiple bands
srf_b2 = get_spectral_response_function(excel_file, 'S2B', 'B02')
srf_b8 = get_spectral_response_function(excel_file, 'S2C', 'B08')

print(f"\nS2B B02 at 493 nm: {srf_b2(493.0):.8f}")
print(f"S2C B08 at 842 nm: {srf_b8(842.0):.8f}")

# Query multiple wavelengths at once
wavelengths = np.arange(600, 700, 10)
responses = [srf_b4(wl) for wl in wavelengths]
print(f"\nS2A B04 responses from 600-690 nm:")
for wl, resp in zip(wavelengths, responses):
    print(f"  {wl} nm: {resp:.6f}")
