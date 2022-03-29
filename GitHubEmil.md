# För att hämta ett repo:  

```py
git clone *address*
```
Se till att du cd'ar in den nya foldern.

### För att hämta en specifik branch
```
git fetch origin *namn på branch*
```
## För att uppdatera en branch
Välj branchen

```
git checkout * namn på branch *
```
För att  hämta (Vet inte vad det är för skillnad på fetch och pull) :
```
git pull
```



# För att göra en commit
```
git add *namn på filen*
```
#### Kollar vilka filer du har lagt till
``` 
git status
```
#### För att commita ändringarna du har lagt till localt
```
git commit -m "*commentar*"
```
#### För att pusha det du har commitat localt till remote
```
git push origin *namn på branch *
```

# För att mergea (pusha) en fil från en branch till en annan
checkout branchen du vill mergea till
```
git checkout <branch_to_merge_into>
```

För att hämta filen du vill mergea
```
git checkout <branch_to_merge_from> -- <file> 
```

sen add,commit,pusha som vanligt.