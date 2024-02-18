using Xunit;
using WordCounter;


public class TestFiles
{

    private readonly TextFile textFile;

    public TestFiles()
    {
        textFile = new TextFile("dummy/path");
    }

    [Fact]
    public void ParseStringToArray_ShouldSplitSpaces()
    {
        string fileContent = "word1 word2 word3";

        string[] result = TextFile.ParseStringToArray(fileContent);

        Assert.Equal(3, result.Length);
        Assert.Equal("word1", result[0]);
        Assert.Equal("word2", result[1]);
        Assert.Equal("word3", result[2]);
    }

    [Fact]
    public void ParseStringToArray_ShouldSplitNewLines()
    {
        string fileContent = "word1\nword2\nword3";

        string[] result = TextFile.ParseStringToArray(fileContent);

        Assert.Equal(3, result.Length);
        Assert.Equal("word1", result[0]);
        Assert.Equal("word2", result[1]);
        Assert.Equal("word3", result[2]);
    }

    [Fact]
    public void ParseStringToArray_ShouldSplitCarriageReturns()
    {
        string fileContent = "word1\rword2\rword3";

        string[] result = TextFile.ParseStringToArray(fileContent);

        Assert.Equal(3, result.Length);
        Assert.Equal("word1", result[0]);
        Assert.Equal("word2", result[1]);
        Assert.Equal("word3", result[2]);
    }

    [Fact]
    public void ParseStringToArray_ShouldSplitDoubleQuote()
    {
        string fileContent = "\"word1\"word2\"word3\"";

        string[] result = TextFile.ParseStringToArray(fileContent);

        Assert.Equal(3, result.Length);
        Assert.Equal("word1", result[0]);
        Assert.Equal("word2", result[1]);
        Assert.Equal("word3", result[2]);
    }

    [Fact]
    public void CountWordsInArray_ShouldReturnTwo()
    {
        textFile.FileName = "DummyName";

        string[] words = ["DummyName", "Woops", "DummyName", "Dummy Name", "World"];

        int result = textFile.CountWordsInArray(words);

        Assert.Equal(2, result);
    }

    [Fact]
    public void PrintWordCount()
    {
        textFile.FileName = "DummyName";
        StringWriter stringWriter = new StringWriter();
        Console.SetOut(stringWriter);

        textFile.PrintWordCount(5);

        string expectedOutput = "The word DummyName appeared 5 times";
        Assert.Equal(expectedOutput, stringWriter.ToString().Trim());
    }
}