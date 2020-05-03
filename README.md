# timewarrior-polybar
A polybar plugin to track timewarrior states, because I always forget to deactivate/activate a current task.
The implementation of this idea has just started. I've put it here because one of the main functionalities I need, which is
showing the current tag, is easily implemented by simply calling the `timew` command.

## Desired functionality:
- [x] show the tag being tracked
- [ ] allow to start a tag tracking
- [ ] allow to stop the current tag tracking
- [ ] toggle for a more detailed view of the current tracking

## Requirements
- polybar
- timew

## How to use

In your config, include the following lines, and customize them as you want:
```
[module/timew]
type = custom/script
label = %output%
tail = true
interval = 1
exec = timew
exec-if = true
format = <label>
format-background = ${colors.background} # a color you want for the text background
format-foreground = ${colors.foreground} # a color you want for the text foreground
format-prefix = "timew "
format-padding = 4
format-prefix-foreground = # a color you want for the 'timew' label
```

Remember to place this module somewhere in your bar, using the bar specific configurations.
