from django.contrib import admin
from core.models import CartOrderProducts, Product, Category, Vendor, CartOrder, ProductImages, ProductReview, wishlist_model, Address,Brand,Size,Color

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_editable = ['title', 'price', 'featured', 'product_status','deals','selling','trending','recent','top']
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid', 'brand','color','size','old_price','deals','selling','trending','recent','top']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
    
    
admin.site.register(Brand)
admin.site.register(Size)


class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']


class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'product_status', 'sku']
    list_display = ['user',  'price', 'paid_status', 'order_date','product_status', 'sku']


class CartOrderProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image','qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','category_image','cid')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
