from django import forms

class SensorNodeForm(forms.Form):
	SensorName = forms.CharField(label='Sensor name', max_length=100)
	ClusterName = forms.CharField(label='Cluster name', max_length=100)
	lat = forms.CharField(label='Latitude', max_length=100)
	lon = forms.CharField(label='Longitude', max_length=100)

	class Meta:
		fields = ['your_name']

class ClusterNodeForm(forms.Form):
	ClusterName = forms.CharField(label='Cluster name', max_length=100)
	lat = forms.CharField(label='Latitude', max_length=100)
	lon = forms.CharField(label='Longitude', max_length=100)

	class Meta:
		fields = ['your_name']

class FarmEditForm(forms.Form):
	farmName = forms.CharField(label='Farm name', max_length=100)
	userName = forms.CharField(label='User name', max_length=100)
	lat = forms.CharField(label='Latitude', max_length=100)
	lon = forms.CharField(label='Longitude', max_length=100)

	class Meta:
		fields = ['your_name']

class NetworkCreationForm(forms.Form):
	networkName = forms.CharField(label='Network name', max_length=100)
	lat = forms.CharField(label='Latitude', max_length=100)
	lon = forms.CharField(label='Longitude', max_length=100)

	class Meta:
		fields = ['your_name']

class NetworkDeletionForm(forms.Form):

	class Meta:
		fields = ['your_name']