### JVM

Bytecodes everywhere, reverse them.

Attachment
rev25\_3100aa76fca4432f.zip 

---

Let's decompile the .class.

    $ javap -c EKO.class

    public class EKO {
      public EKO();
        Code:
           0: aload_0
           1: invokespecial #1                  // Method java/lang/Object."<init>":()V
           4: return

      public static void main(java.lang.String[]);
        Code:
           0: iconst_0
           1: istore_1
           2: iconst_0
           3: istore_2
           4: iload_2
           5: sipush        1337
           8: if_icmpge     21
          11: iload_1
          12: iload_2
          13: iadd
          14: istore_1
          15: iinc          2, 1
          18: goto          4
          21: new           #2                  // class java/lang/StringBuilder
          24: dup
          25: invokespecial #3                  // Method java/lang/StringBuilder."<init>":()V
          28: ldc           #4                  // String EKO{
          30: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
          33: iload_1
          34: invokevirtual #6                  // Method java/lang/StringBuilder.append:(I)Ljava/lang/StringBuilder;
          37: ldc           #7                  // String }
          39: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
          42: invokevirtual #8                  // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
          45: astore_2
          46: return
    }

We see that we have, from offset 28 to 37, the strings "EKO{" and "}" separated by a StringBuilder. So the flag was probably created with the instruction `"EKO{" + value + "}"`.

We need to find the value put inside.

The code between offset 0 and 18 is the following :

    int var1 = 0; // stored at 1
    int var2 = 0; // stored at 2
    while (var2 < 1337) {
        var1 += var2;
        var2++;
    }

So var1 = sum(range(1337)) = 893116

Flag : `EKO{893116}`
