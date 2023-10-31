from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import User
from flask_wtf.file import FileField, FileRequired

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Already Exist')
    def validate_email_addr(self, email_addr_to_check):
        email_addr=User.query.filter_by(email_addr=email_addr_to_check.data).first()
        if email_addr:
            raise ValidationError('Email Already Exist')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_addr = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username= StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Sign in')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(label='Old Password:', validators=[Length(min=6), DataRequired()])
    new_password = PasswordField(label='New Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[Length(min=6), DataRequired()])
    change = SubmitField(label='Change Password')


class ShopItemForm(FlaskForm):
    product_name = StringField(label='Product Name:', validators=[Length(min=2, max=50), DataRequired()])
    price = FloatField(label='Price:', validators=[DataRequired()])
    in_stock = IntegerField(label='In Stock', validators=[DataRequired()])
    product_image = FileField(label='Product Image', validators=[FileRequired()])
    add_product = SubmitField(label='Add Product')
    update_product = SubmitField(label='Update Product')

class OrderForm(FlaskForm):
    order_status = SelectField('Order Status', choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'),
                                                        ('Out for delivery', 'Out for delivery'),
                                                        ('Delivered', 'Delivered'), ('Canceled', 'Canceled')])

    update = SubmitField('Update Status')
