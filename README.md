If you use [Visual Studio Code](https://code.visualstudio.com), in the [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools), you can create "tasks.json" and "launch.json" as instructed, and then debug line by line.

## 配置调试环境

假设你有一个简单的C++程序，代码如下：[example.cpp](https://github.com/SHI200005/Examples/blob/main/debug/example.cpp)。

## 配置 tasks.json

**配置任务**：编译C++程序

- 按下 Ctrl+Shift+B（Windows/Linux）或 Cmd+Shift+B（Mac），如果没有配置编译任务，VSCode会提示你选择任务。
- 选择 “C++: g++ build active file”（假设你安装了 g++）。
- 如果这是你第一次配置，VSCode会创建一个 .vscode 文件夹，并生成一个 tasks.json 文件来配置编译过程。例如，[tasks.json](https://github.com/SHI200005/Examples/blob/main/debug/.vscode/tasks.json)。

## 配置调试

创建 [launch.json](https://github.com/SHI200005/Examples/blob/main/debug/.vscode/launch.json)

- 按 F5 或点击左侧的“运行和调试”图标，然后选择“创建一个 launch.json 文件”。
- 选择 C++ (GDB/LLDB)，如果你在Mac上，选择 LLDB；如果在Windows上，选择 GDB。
- 配置文件会自动生成，包含了调试的基本信息。通常生成的配置如下：

## 设置断点

1. 在你的C++代码中，点击行号左侧的空白区域，这里会显示一个红点，表示设置了一个断点。
   - 比如，你可以在 cout << "Result: " << add_numbers(x, y) << endl; 这一行设置断点。

## 启动调试

1. **编译代码**：按 Ctrl+Shift+B 编译 C++ 代码，确保没有编译错误。
2. **启动调试**：按 F5 或点击左侧的“绿色三角形”按钮来启动调试。程序会在你设置的断点处暂停。
   - 你可以在“调试”面板中查看“变量”部分，监控 x 和 y 的值，发现 y 被设置成了负数。

## 调试过程

- **查看变量**：在“调试”面板下，点击“变量”查看当前变量的值（例如：x = 10, y = -5）。
- **逐步执行**：你可以使用调试按钮来逐步执行代码：
  - **Step Over**（逐行执行）: 点击左上角的“Step Over”按钮，程序会逐行执行。
  - **Step Into**（进入函数内部）: 点击“Step Into”按钮，程序会进入函数内部执行（例如进入 add_numbers 函数）。
  - **Continue**（继续执行）：点击“Continue”按钮，程序会继续执行，直到下一个断点或者程序结束。

## 输出和调试控制台

- 调试过程中，所有的输出都会显示在“调试控制台”中，你可以查看程序打印的内容，或者调试命令的执行结果。