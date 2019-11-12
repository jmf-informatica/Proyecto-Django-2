from django import forms
from pruebas.models import Productos, Paises, Periodos


class FormProductos(forms.ModelForm):
    #nombre=forms.ModelChoiceField(queryset=Productos.objects.values_list('nombre', flat=True).distinct(), label='')
    nombre=forms.ModelChoiceField(queryset=None, label="", empty_label='Seleccione un Plan', required=False)
   
    class Meta:
        model=Productos
        fields=['nombre']
        labels={'nombre':''}



    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'js-example-basic-single',
                'style':'width: 300px;'

        })
        self.fields['nombre'].queryset=Productos.objects.values_list('nombre', flat=True).distinct()

class FormPeriodos(forms.ModelForm):
    periodo=forms.ModelChoiceField(queryset=Periodos.objects.all(), label='', empty_label='Seleccione un periodo',required=False)
    
    
    class Meta:
        model=Periodos
        fields=['periodo']
        labels={'periodo':''}

    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'js-example-basic-single',
                'style':'width: 300px;'
                
        })

class FormPaises(forms.ModelForm):
    pais=forms.ModelChoiceField(queryset=Paises.objects.all(), label='', empty_label='Seleccione un pais',required=False)
    
    
    class Meta:
        model=Paises
        fields=['pais']
        labels={'pais':''}

    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'js-example-basic-single',
                'style':'width: 300px;'
                
        })

class FormCreate(forms.ModelForm):
    #Lista_periodos=[('0','Seleccione un periodo'),('Mensual','Mensual'),('Trimestral','Trimestral'),('Semestral','Semestral'),('Anual','Anual'),('Bianual','Bianual'),('5 años','5 años')]
    #Lista_paises=[('0','Seleccione un país'),('Argentina','Argentina'),('Venezuela','Venezuela'),('Chile','Chile'),('Uruguay','Uruguay'),('Peru','Peru')]
    #Lista_id=[('Mensual','1 - Mensual'),('Trimestral','2 - Trimestral'),('Semestral','3 - Semestral'),('Anual','4 - Anual'),('Bianual','5 - Bianual'),('5 años','6 - 5años')]
    
    #pais=forms.ChoiceField(choices=(Lista_paises), label='Residencia',initial='Seleccione un país')
    #periodo=forms.ChoiceField(choices=(Lista_periodos), label='Periodo de pago', initial='Seleccione un periodo')
    #id_periodo=forms.ChoiceField(choices=(Lista_id), label='ID Periodo de pago', initial='Seleccione ID correspondiente')
    
    
    #pais=forms.ModelChoiceField(queryset=Productos_Arg.objects.values_list('pais', flat=True).distinct('pais'), label='Residencia', to_field_name="pais", empty_label='Seleccione un país')
    #id_periodo=forms.ModelChoiceField(queryset=Productos_Arg.objects.values_list('id_periodo', flat=True).distinct('id_periodo'), label='ID periodo de pago', to_field_name="id_periodo", empty_label='Seleccione un ID')
    #periodo=forms.ModelChoiceField(queryset=Productos_Arg.objects.values_list('periodo', flat=True).order_by('id_periodo').distinct('id_periodo'), empty_label='Seleccione un periodo')
    #peroido=forms.TextInput(attrs={'readonly':'readonly'})
    
    periodo=forms.ModelChoiceField(queryset=Periodos.objects.all(), empty_label='Seleccione un periodo', label='')
    pais=forms.ModelChoiceField(queryset=Paises.objects.all(),empty_label='Seleccione un pais',label='')
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Escriba la descripcion del producto'}), label='')

    
    class Meta:
        model=Productos

        fields=['nombre','periodo','pais','descripcion','PrecioCompra','PrecioRenovacion']
        labels={
            'nombre':'',
            'PrecioCompra':'',
            'PrecioRenovacion':'',
            'descripcion':'',
        }


    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                
         })
        self.fields['nombre'].widget.attrs.update({
             'placeholder':'Escriba nombre del plan'})
        self.fields['PrecioCompra'].widget.attrs.update({
             'placeholder':'Escriba precio de compra'})
        self.fields['PrecioRenovacion'].widget.attrs.update({
             'placeholder':'Escriba precio de renovacion'})


    

    