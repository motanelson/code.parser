using System;

class MainApp
{
    static void ddebugs(string a){
        string s="";
        Console.WriteLine(a+"\nwait a key enter.");
        s=Console.ReadLine()+"";
        s=s+"";
     }

    public static void Main()
    {
        int i=0;
        for(i=0;i<10;i++)ddebugs(i.ToString());

    }
}



