#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;
int main ()
{
int i;
cout &lt;&lt; &quot;Please enter an integer value: &quot;;
cin &gt;&gt; i;
cout &lt;&lt; &quot;The value you entered is &quot; &lt;&lt; i;
cout &lt;&lt; &quot; and its double is &quot; &lt;&lt; i*2 &lt;&lt;
&quot;.\n&quot;;
string mystr;
cout &lt;&lt; &quot;What&#39;s your name? &quot;;
getline (cin, mystr);
cout &lt;&lt; &quot;Hello &quot; &lt;&lt; mystr &lt;&lt; &quot;.\n&quot;;
return 0;
}
