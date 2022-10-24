# conda-dependency-builds-bug
Example code to reproduce a bug in conda. It installs different builds depending on whether the package is set as a dependency on the environment file or as a dependency from another package.

## Steps to reproduce

1. Install both environments with _conda install -n "environmentname" --file "environmentfile"_.
2. Activate the environments with _conda activate "environmentname"_
3. Use _conda list_ to see the packages installed. You will see that the package lxml uses 2 different builds: __py37h540881e_3__ for the environmentcorrect.yml and __py37h540881e_2__ for the environmentincorrect.yml.
4. Run _python3 test.py_ in each environment to see the outputs. They should be:

<table>
<tr>
<td>
Correct
</td>
<td>
Incorrect
</td>
</tr>
<tr>
<td valign="top">

```
<PanelDescription>
        <name>Example</name>
        <classname>TaurusForm</classname>
        <modulename/>
        <widgetname/>
        <floating>False</floating>
        <sharedDataWrite/>
        <sharedDataRead/>
        <model/>
</PanelDescription>
```

</td>
<td valign="top">

```
<PanelDescription>
        <name>Example</name>
        <classname>TaurusForm</classname>
        <modulename/>
        <widgetname/>
        <floating>False</floating>
        <sharedDataWrite/>
        <sharedDataRead/>
        <model/>
    </PanelDescription>
  </PanelDescriptions>
</taurusgui_config>

```   

</td>
</tr>
</table>


As you can see the output of the code (that prints the result of _find()_ method from lxml) is different. In fact, the incorrect one returns an invalid xml, causing an error when trying to parse it.  
The build __py37h540881e_2__ contains an error on that method. But conda shoudn't install it when lxml is a dependency of another package. It should install the latest build, the same one that is installed when we set lxml as the explicit dependency in the environment file.