using System;

class MainApp
{

    static String concats(String a,String b,String c){
       return a+b+c;
    }

    public static void Main()
    {
        String s=concats("Hello","," ," World!");

        Console.WriteLine(s);

    }
}
