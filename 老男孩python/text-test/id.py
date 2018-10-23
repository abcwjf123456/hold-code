# id(object)
#
# 功能：返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。
# 此处所说的对象应该特指复合类型的对象(如类、list等)，对于字符串、整数等类型，变量的id是随值的改变而改变的。

# 用is判断两个对象是否相等时，依据就是这个id值
#
# is与==的区别就是，is是内存中的比较，而==是值的比较


#我没有对id进行练习