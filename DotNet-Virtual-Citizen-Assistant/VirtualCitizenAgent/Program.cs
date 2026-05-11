using VirtualCitizenAgent.Configuration;
using VirtualCitizenAgent.Services;

var builder = WebApplication.CreateBuilder(args);

// Configuration
builder.Services.Configure<SearchConfiguration>(
    builder.Configuration.GetSection(SearchConfiguration.SectionName));
builder.Services.Configure<FoundryConfiguration>(
    builder.Configuration.GetSection(FoundryConfiguration.SectionName));

// Services
builder.Services.AddSingleton<ISearchService, SearchService>();
builder.Services.AddSingleton<IChatService, ChatService>();
builder.Services.AddSingleton<ICategoryService, CategoryService>();

// MVC
builder.Services.AddControllersWithViews();

// API documentation
builder.Services.AddEndpointsApiExplorer();

// CORS for API access
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseCors("AllowAll");
app.UseAuthorization();

// API routes
app.MapControllers();

// MVC routes
app.MapControllerRoute(
    name: "chat",
    pattern: "chat",
    defaults: new { controller = "ChatView", action = "Index" });

app.MapControllerRoute(
    name: "search",
    pattern: "search",
    defaults: new { controller = "SearchView", action = "Index" });

app.MapControllerRoute(
    name: "categories",
    pattern: "categories/{id?}",
    defaults: new { controller = "CategoriesView", action = "Index" });

app.MapControllerRoute(
    name: "documents",
    pattern: "documents/{id}",
    defaults: new { controller = "Documents", action = "Details" });

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();

// Make Program class accessible for integration tests
public partial class Program { }
