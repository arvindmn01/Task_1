import pyvips

# image=pyvips.Image.new_from_file('Reactive hyperplasia.svs')
image=pyvips.Image.new_from_file('Normal Lymphnode.svs')
image.dzsave('Normal Lymphnode')