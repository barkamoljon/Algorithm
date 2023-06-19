import numpy as np

def fourier_transform(signal):
  """
  Performs the Fourier transform on a signal.

  Args:
    signal: A NumPy array representing the signal.

  Returns:
    A NumPy array representing the Fourier transform of the signal.
  """
  # Calculate the length of the signal
  n = len(signal)
  
  # Create a complex array to store the Fourier transform
  ft = np.fft.fft(signal)
  
  # Return the transform
  return ft

# Generate a simple signal.
signal = np.sin(2 * np.pi * np.linspace(0, 1, 100))

# Calculate the Fourier transform of the signal.
ft = fourier_transform(signal)

# Plot the signal and its Fourier transform.
plt.plot(signal)
plt.plot(ft.real, label='Real')
plt.plot(ft.imag, label='Imaginary')
plt.legend()
plt.show()
