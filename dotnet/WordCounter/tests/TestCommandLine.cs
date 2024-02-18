using Xunit;
using WordCounter;


public class TestCommandLine
{
    [Fact]
    public void IsValidArgument_ReturnsTrue()
    {
        // Given
        string[] args = ["validPath.txt"];

        // When
        bool result = InputArgument.IsValidArgument(args);

        // Then
        Assert.True(result);
    }

    [Fact]
    public void IsValidArgument_NoArgument()
    {
        // Given
        string[] args = [];

        // When
        var exception = Assert.Throws<ArgumentException>(() => InputArgument.IsValidArgument(args));
        
        // Then
        Assert.Equal("Path was not provided as argument", exception.Message);
    }

    [Fact]
    public void IsValidArgument_TooManyArguments()
    {
        // Given
        string[] args = ["path/one", "path/two"];
        
        // When
        var exception = Assert.Throws<ArgumentException>(() => InputArgument.IsValidArgument(args));

        // Then
        Assert.Equal("Program only takes one path as argument", exception.Message);
    }

    [Fact]
    public void IsValidArgument_PathHasWrongExtension()
    {
        // Given
        string[] args = ["path/has/wrong/extension.jpeg"];   
        
        // When
        var exception = Assert.Throws<ArgumentException>(() => InputArgument.IsValidArgument(args));

        // Then
        Assert.Equal("path/has/wrong/extension.jpeg has the wrong extension", exception.Message);
    }

    [Fact]
    public void IsValidArgument_FileNameHasSpaces()
    {
        // Given
        string[] args = ["dummy/path/file name.txt"];
        
        // When
        var exception = Assert.Throws<ArgumentException>(() => InputArgument.IsValidArgument(args));

        // Then
        Assert.Equal("dummy/path/file name.txt has spaces in file name", exception.Message);
    }

    [Fact]
    public void IsValidExtension_ReturnTrue()
    {
        // Given
        string filePath = "dummy/path/file.txt";

        // When
        bool result = InputArgument.IsValidExtension(filePath);

        // Then
        Assert.True(result);
    }

        [Fact]
    public void IsValidExtension_ReturnFalse()
    {
        // Given
        string filePath = "dummy/path/file.png";

        // When
        bool result = InputArgument.IsValidExtension(filePath);

        // Then
        Assert.False(result);
    }

    [Fact]
    public void FileHasNoSpaces_ReturnTrue()
    {
        // Given
        string filePath = "dummy/path/textfile.txt";

        // When
        bool result = InputArgument.FileHasNoSpaces(filePath);

        // Then
        Assert.True(result);
    }

    [Fact]
    public void FileHasNoSpaces_ReturnFalse()
    {
        // Given
        string filePath = "dummy/path/text file.txt";

        // When
        bool result = InputArgument.FileHasNoSpaces(filePath);

        // Then
        Assert.False(result);
    }
}
